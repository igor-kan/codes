; ModuleID = 'algorithms/02_c/math/sieve.c'
source_filename = "algorithms/02_c/math/sieve.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [4 x i8] c"%d \00", align 1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local void @sieve(i32 noundef %0) local_unnamed_addr #0 {
  %2 = add i32 %0, 1
  %3 = zext i32 %2 to i64
  %4 = alloca i8, i64 %3, align 16
  call void @llvm.memset.p0.i64(ptr nonnull align 16 %4, i8 1, i64 %3, i1 false)
  %5 = getelementptr inbounds nuw i8, ptr %4, i64 1
  store i8 0, ptr %5, align 1, !tbaa !9
  %6 = sext i32 %0 to i64
  %7 = icmp slt i32 %0, 4
  br i1 %7, label %8, label %10

8:                                                ; preds = %29, %1
  %9 = icmp slt i32 %0, 2
  br i1 %9, label %35, label %36

10:                                               ; preds = %1, %29
  %11 = phi i64 [ %30, %29 ], [ 2, %1 ]
  %12 = phi i32 [ %34, %29 ], [ 4, %1 ]
  %13 = phi i32 [ %33, %29 ], [ 5, %1 ]
  %14 = getelementptr inbounds nuw i8, ptr %4, i64 %11
  %15 = load i8, ptr %14, align 1, !tbaa !9
  %16 = icmp eq i8 %15, 0
  %17 = mul nuw nsw i64 %11, %11
  %18 = trunc nuw i64 %17 to i32
  %19 = icmp slt i32 %0, %18
  %20 = select i1 %16, i1 true, i1 %19
  br i1 %20, label %29, label %21

21:                                               ; preds = %10
  %22 = zext i32 %12 to i64
  br label %23

23:                                               ; preds = %21, %23
  %24 = phi i64 [ %22, %21 ], [ %26, %23 ]
  %25 = getelementptr inbounds nuw i8, ptr %4, i64 %24
  store i8 0, ptr %25, align 1, !tbaa !9
  %26 = add nuw nsw i64 %24, %11
  %27 = trunc nuw i64 %26 to i32
  %28 = icmp slt i32 %0, %27
  br i1 %28, label %29, label %23, !llvm.loop !10

29:                                               ; preds = %23, %10
  %30 = add nuw nsw i64 %11, 1
  %31 = mul nuw nsw i64 %30, %30
  %32 = icmp sgt i64 %31, %6
  %33 = add i32 %13, 2
  %34 = add i32 %12, %13
  br i1 %32, label %8, label %10, !llvm.loop !12

35:                                               ; preds = %44, %8
  ret void

36:                                               ; preds = %8, %44
  %37 = phi i64 [ %45, %44 ], [ 2, %8 ]
  %38 = getelementptr inbounds nuw i8, ptr %4, i64 %37
  %39 = load i8, ptr %38, align 1, !tbaa !9
  %40 = icmp eq i8 %39, 0
  br i1 %40, label %44, label %41

41:                                               ; preds = %36
  %42 = trunc nuw nsw i64 %37 to i32
  %43 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str, i32 noundef %42)
  br label %44

44:                                               ; preds = %36, %41
  %45 = add nuw nsw i64 %37, 1
  %46 = icmp eq i64 %45, %3
  br i1 %46, label %35, label %36, !llvm.loop !13
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: write)
declare void @llvm.memset.p0.i64(ptr writeonly captures(none), i8, i64, i1 immarg) #1

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #2

attributes #0 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: write) }
attributes #2 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!7, !7, i64 0}
!10 = distinct !{!10, !11}
!11 = !{!"llvm.loop.mustprogress"}
!12 = distinct !{!12, !11}
!13 = distinct !{!13, !11}
