; ModuleID = 'algorithms/02_c/dp/longest_palindromic_subsequence.c'
source_filename = "algorithms/02_c/dp/longest_palindromic_subsequence.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@dp = internal unnamed_addr global [1001 x [1001 x i32]] zeroinitializer, align 16
@str = private unnamed_addr constant [49 x i8] c"[C LPS] Longest palindromic subsequence verified\00", align 1
@str.5 = private unnamed_addr constant [26 x i8] c"[C LPS] FAILED: cbbd -> 2\00", align 1
@str.6 = private unnamed_addr constant [27 x i8] c"[C LPS] FAILED: bbbab -> 4\00", align 1

; Function Attrs: nofree norecurse nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local i32 @longest_palindromic_subsequence(ptr noundef readonly captures(none) %0) local_unnamed_addr #0 {
  %2 = tail call i64 @strlen(ptr noundef nonnull dereferenceable(1) %0) #5
  %3 = trunc i64 %2 to i32
  %4 = add i32 %3, -1
  %5 = icmp sgt i32 %3, 0
  br i1 %5, label %6, label %10

6:                                                ; preds = %1
  %7 = and i64 %2, 2147483647
  %8 = zext nneg i32 %4 to i64
  %9 = and i64 %2, 2147483647
  br label %14

10:                                               ; preds = %25, %1
  %11 = sext i32 %4 to i64
  %12 = getelementptr inbounds i32, ptr @dp, i64 %11
  %13 = load i32, ptr %12, align 4, !tbaa !5
  ret i32 %13

14:                                               ; preds = %6, %25
  %15 = phi i64 [ %8, %6 ], [ %26, %25 ]
  %16 = phi i64 [ %7, %6 ], [ %28, %25 ]
  %17 = getelementptr inbounds nuw [1001 x i32], ptr @dp, i64 %15
  %18 = getelementptr inbounds nuw i32, ptr %17, i64 %15
  store i32 1, ptr %18, align 4, !tbaa !5
  %19 = add nuw nsw i64 %15, 1
  %20 = icmp slt i64 %19, %9
  br i1 %20, label %21, label %25

21:                                               ; preds = %14
  %22 = getelementptr inbounds nuw i8, ptr %0, i64 %15
  %23 = load i8, ptr %22, align 1, !tbaa !9
  %24 = getelementptr inbounds nuw [1001 x i32], ptr @dp, i64 %19
  br label %29

25:                                               ; preds = %46, %14
  %26 = add nsw i64 %15, -1
  %27 = icmp sgt i64 %15, 0
  %28 = add nsw i64 %16, -1
  br i1 %27, label %14, label %10, !llvm.loop !10

29:                                               ; preds = %21, %46
  %30 = phi i64 [ %16, %21 ], [ %47, %46 ]
  %31 = getelementptr inbounds nuw i8, ptr %0, i64 %30
  %32 = load i8, ptr %31, align 1, !tbaa !9
  %33 = icmp eq i8 %23, %32
  %34 = getelementptr i32, ptr %24, i64 %30
  br i1 %33, label %35, label %40

35:                                               ; preds = %29
  %36 = getelementptr i8, ptr %34, i64 -4
  %37 = load i32, ptr %36, align 4, !tbaa !5
  %38 = add nsw i32 %37, 2
  %39 = getelementptr inbounds nuw i32, ptr %17, i64 %30
  store i32 %38, ptr %39, align 4, !tbaa !5
  br label %46

40:                                               ; preds = %29
  %41 = load i32, ptr %34, align 4, !tbaa !5
  %42 = getelementptr i32, ptr %17, i64 %30
  %43 = getelementptr i8, ptr %42, i64 -4
  %44 = load i32, ptr %43, align 4, !tbaa !5
  %45 = tail call i32 @llvm.smax.i32(i32 %41, i32 %44)
  store i32 %45, ptr %42, align 4, !tbaa !5
  br label %46

46:                                               ; preds = %35, %40
  %47 = add nuw nsw i64 %30, 1
  %48 = trunc nuw i64 %47 to i32
  %49 = icmp slt i32 %48, %3
  br i1 %49, label %29, label %25, !llvm.loop !12
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: read)
declare i64 @strlen(ptr noundef captures(none)) local_unnamed_addr #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 16032), align 16, !tbaa !5
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 12024), align 8, !tbaa !5
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 12028), align 4, !tbaa !5
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8016), align 16, !tbaa !5
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8020), align 4, !tbaa !5
  store i32 3, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8024), align 8, !tbaa !5
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4008), align 8, !tbaa !5
  %1 = load i32, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8012), align 4, !tbaa !5
  %2 = add nsw i32 %1, 2
  store i32 %2, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4012), align 4, !tbaa !5
  %3 = tail call i32 @llvm.smax.i32(i32 %2, i32 1)
  store i32 %3, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4016), align 16, !tbaa !5
  %4 = load i32, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8020), align 4, !tbaa !5
  %5 = add nsw i32 %4, 2
  store i32 %5, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4020), align 4, !tbaa !5
  store i32 1, ptr @dp, align 16, !tbaa !5
  %6 = load i32, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4004), align 4, !tbaa !5
  %7 = add nsw i32 %6, 2
  store i32 %7, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4), align 4, !tbaa !5
  store i32 3, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8), align 8, !tbaa !5
  %8 = load i32, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4016), align 16, !tbaa !5
  %9 = tail call i32 @llvm.smax.i32(i32 %8, i32 3)
  store i32 %9, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 12), align 4, !tbaa !5
  %10 = add nsw i32 %8, 2
  store i32 %10, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 16), align 16, !tbaa !5
  %11 = icmp eq i32 %10, 4
  br i1 %11, label %12, label %20

12:                                               ; preds = %0
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8016), align 16, !tbaa !5
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8020), align 4, !tbaa !5
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4008), align 8, !tbaa !5
  %13 = load i32, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8012), align 4, !tbaa !5
  %14 = add nsw i32 %13, 2
  store i32 %14, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4012), align 4, !tbaa !5
  %15 = tail call i32 @llvm.smax.i32(i32 %14, i32 1)
  store i32 %15, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4016), align 16, !tbaa !5
  store i32 1, ptr @dp, align 16, !tbaa !5
  store i32 1, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 4), align 4, !tbaa !5
  %16 = tail call i32 @llvm.smax.i32(i32 %14, i32 1)
  store i32 %16, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 8), align 8, !tbaa !5
  store i32 %15, ptr getelementptr inbounds nuw (i8, ptr @dp, i64 12), align 4, !tbaa !5
  %17 = icmp ne i32 %13, 0
  %18 = select i1 %17, ptr @str.5, ptr @str
  %19 = zext i1 %17 to i32
  br label %20

20:                                               ; preds = %12, %0
  %21 = phi ptr [ @str.6, %0 ], [ %18, %12 ]
  %22 = phi i32 [ 1, %0 ], [ %19, %12 ]
  %23 = tail call i32 @puts(ptr nonnull dereferenceable(1) %21)
  ret i32 %22
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #3

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smax.i32(i32, i32) #4

attributes #0 = { nofree norecurse nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: read) "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind }
attributes #4 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #5 = { nounwind willreturn memory(read) }

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
