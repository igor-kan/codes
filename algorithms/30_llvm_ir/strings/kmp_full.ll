; ModuleID = 'algorithms/02_c/strings/kmp_full.c'
source_filename = "algorithms/02_c/strings/kmp_full.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [29 x i8] c"ABABDABACDABABCABABABABCABAB\00", align 1
@.str.1 = private unnamed_addr constant [10 x i8] c"ABABCABAB\00", align 1
@.str.2 = private unnamed_addr constant [11 x i8] c"found == 2\00", align 1
@.str.3 = private unnamed_addr constant [35 x i8] c"algorithms/02_c/strings/kmp_full.c\00", align 1
@__PRETTY_FUNCTION__.main = private unnamed_addr constant [15 x i8] c"int main(void)\00", align 1
@.str.4 = private unnamed_addr constant [17 x i8] c"matches[0] == 10\00", align 1
@.str.5 = private unnamed_addr constant [17 x i8] c"matches[1] == 19\00", align 1
@.str.6 = private unnamed_addr constant [48 x i8] c"[C KMP] Matches verified at offsets: %d and %d\0A\00", align 1

; Function Attrs: nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable
define dso_local void @compute_lps(ptr noundef readonly captures(none) %0, i32 noundef %1, ptr noundef captures(none) initializes((0, 4)) %2) local_unnamed_addr #0 {
  store i32 0, ptr %2, align 4, !tbaa !5
  %4 = icmp sgt i32 %1, 1
  br i1 %4, label %5, label %32

5:                                                ; preds = %3, %28
  %6 = phi i32 [ %30, %28 ], [ 1, %3 ]
  %7 = phi i32 [ %29, %28 ], [ 0, %3 ]
  %8 = sext i32 %6 to i64
  %9 = getelementptr inbounds i8, ptr %0, i64 %8
  %10 = load i8, ptr %9, align 1, !tbaa !9
  %11 = sext i32 %7 to i64
  %12 = getelementptr inbounds i8, ptr %0, i64 %11
  %13 = load i8, ptr %12, align 1, !tbaa !9
  %14 = icmp eq i8 %10, %13
  br i1 %14, label %15, label %19

15:                                               ; preds = %5
  %16 = add nsw i32 %7, 1
  %17 = getelementptr inbounds i32, ptr %2, i64 %8
  store i32 %16, ptr %17, align 4, !tbaa !5
  %18 = add nsw i32 %6, 1
  br label %28

19:                                               ; preds = %5
  %20 = icmp eq i32 %7, 0
  br i1 %20, label %25, label %21

21:                                               ; preds = %19
  %22 = getelementptr i32, ptr %2, i64 %11
  %23 = getelementptr i8, ptr %22, i64 -4
  %24 = load i32, ptr %23, align 4, !tbaa !5
  br label %28

25:                                               ; preds = %19
  %26 = getelementptr inbounds i32, ptr %2, i64 %8
  store i32 0, ptr %26, align 4, !tbaa !5
  %27 = add nsw i32 %6, 1
  br label %28

28:                                               ; preds = %21, %25, %15
  %29 = phi i32 [ %16, %15 ], [ %24, %21 ], [ 0, %25 ]
  %30 = phi i32 [ %18, %15 ], [ %6, %21 ], [ %27, %25 ]
  %31 = icmp slt i32 %30, %1
  br i1 %31, label %5, label %32, !llvm.loop !10

32:                                               ; preds = %28, %3
  ret void
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nounwind sspstrong memory(readwrite, target_mem0: none, target_mem1: none) uwtable
define dso_local i32 @kmp_search(ptr noundef readonly captures(none) %0, ptr noundef readonly captures(none) %1, ptr noundef writeonly captures(none) %2, i32 noundef %3) local_unnamed_addr #2 {
  %5 = tail call i64 @strlen(ptr noundef nonnull dereferenceable(1) %0) #9
  %6 = trunc i64 %5 to i32
  %7 = tail call i64 @strlen(ptr noundef nonnull dereferenceable(1) %1) #9
  %8 = trunc i64 %7 to i32
  %9 = icmp eq i32 %8, 0
  %10 = icmp eq i32 %6, 0
  %11 = select i1 %9, i1 true, i1 %10
  br i1 %11, label %101, label %12

12:                                               ; preds = %4
  %13 = shl i64 %7, 32
  %14 = ashr exact i64 %13, 30
  %15 = tail call noalias ptr @malloc(i64 noundef %14) #10
  store i32 0, ptr %15, align 4, !tbaa !5
  %16 = icmp sgt i32 %8, 1
  br i1 %16, label %17, label %44

17:                                               ; preds = %12, %40
  %18 = phi i32 [ %42, %40 ], [ 1, %12 ]
  %19 = phi i32 [ %41, %40 ], [ 0, %12 ]
  %20 = sext i32 %18 to i64
  %21 = getelementptr inbounds i8, ptr %1, i64 %20
  %22 = load i8, ptr %21, align 1, !tbaa !9
  %23 = sext i32 %19 to i64
  %24 = getelementptr inbounds i8, ptr %1, i64 %23
  %25 = load i8, ptr %24, align 1, !tbaa !9
  %26 = icmp eq i8 %22, %25
  br i1 %26, label %27, label %31

27:                                               ; preds = %17
  %28 = add nsw i32 %19, 1
  %29 = getelementptr inbounds i32, ptr %15, i64 %20
  store i32 %28, ptr %29, align 4, !tbaa !5
  %30 = add nsw i32 %18, 1
  br label %40

31:                                               ; preds = %17
  %32 = icmp eq i32 %19, 0
  br i1 %32, label %37, label %33

33:                                               ; preds = %31
  %34 = getelementptr i32, ptr %15, i64 %23
  %35 = getelementptr i8, ptr %34, i64 -4
  %36 = load i32, ptr %35, align 4, !tbaa !5
  br label %40

37:                                               ; preds = %31
  %38 = getelementptr inbounds i32, ptr %15, i64 %20
  store i32 0, ptr %38, align 4, !tbaa !5
  %39 = add nsw i32 %18, 1
  br label %40

40:                                               ; preds = %37, %33, %27
  %41 = phi i32 [ %28, %27 ], [ %36, %33 ], [ 0, %37 ]
  %42 = phi i32 [ %30, %27 ], [ %18, %33 ], [ %39, %37 ]
  %43 = icmp slt i32 %42, %8
  br i1 %43, label %17, label %44, !llvm.loop !10

44:                                               ; preds = %40, %12
  %45 = icmp sgt i32 %6, 0
  br i1 %45, label %46, label %99

46:                                               ; preds = %44
  %47 = shl i64 %7, 32
  %48 = ashr exact i64 %47, 30
  %49 = getelementptr i8, ptr %15, i64 %48
  %50 = getelementptr i8, ptr %49, i64 -4
  br label %51

51:                                               ; preds = %46, %94
  %52 = phi i32 [ %97, %94 ], [ 0, %46 ]
  %53 = phi i32 [ %96, %94 ], [ 0, %46 ]
  %54 = phi i32 [ %95, %94 ], [ 0, %46 ]
  %55 = sext i32 %53 to i64
  %56 = getelementptr inbounds i8, ptr %0, i64 %55
  %57 = load i8, ptr %56, align 1, !tbaa !9
  %58 = sext i32 %52 to i64
  %59 = getelementptr inbounds i8, ptr %1, i64 %58
  %60 = load i8, ptr %59, align 1, !tbaa !9
  %61 = icmp eq i8 %57, %60
  %62 = zext i1 %61 to i32
  %63 = add nsw i32 %53, %62
  %64 = add nsw i32 %52, %62
  %65 = icmp eq i32 %64, %8
  br i1 %65, label %66, label %76

66:                                               ; preds = %51
  %67 = icmp slt i32 %54, %3
  br i1 %67, label %68, label %73

68:                                               ; preds = %66
  %69 = sub nsw i32 %63, %8
  %70 = add nsw i32 %54, 1
  %71 = sext i32 %54 to i64
  %72 = getelementptr inbounds i32, ptr %2, i64 %71
  store i32 %69, ptr %72, align 4, !tbaa !5
  br label %73

73:                                               ; preds = %68, %66
  %74 = phi i32 [ %70, %68 ], [ %54, %66 ]
  %75 = load i32, ptr %50, align 4, !tbaa !5
  br label %94

76:                                               ; preds = %51
  %77 = icmp slt i32 %63, %6
  br i1 %77, label %78, label %94

78:                                               ; preds = %76
  %79 = sext i32 %63 to i64
  %80 = getelementptr inbounds i8, ptr %0, i64 %79
  %81 = load i8, ptr %80, align 1, !tbaa !9
  %82 = sext i32 %64 to i64
  %83 = getelementptr inbounds i8, ptr %1, i64 %82
  %84 = load i8, ptr %83, align 1, !tbaa !9
  %85 = icmp eq i8 %81, %84
  br i1 %85, label %94, label %86

86:                                               ; preds = %78
  %87 = icmp eq i32 %64, 0
  br i1 %87, label %92, label %88

88:                                               ; preds = %86
  %89 = getelementptr i32, ptr %15, i64 %82
  %90 = getelementptr i8, ptr %89, i64 -4
  %91 = load i32, ptr %90, align 4, !tbaa !5
  br label %94

92:                                               ; preds = %86
  %93 = add nsw i32 %63, 1
  br label %94

94:                                               ; preds = %76, %78, %92, %88, %73
  %95 = phi i32 [ %74, %73 ], [ %54, %88 ], [ %54, %92 ], [ %54, %78 ], [ %54, %76 ]
  %96 = phi i32 [ %63, %73 ], [ %63, %88 ], [ %93, %92 ], [ %63, %78 ], [ %63, %76 ]
  %97 = phi i32 [ %75, %73 ], [ %91, %88 ], [ 0, %92 ], [ %64, %78 ], [ %64, %76 ]
  %98 = icmp slt i32 %96, %6
  br i1 %98, label %51, label %99, !llvm.loop !12

99:                                               ; preds = %94, %44
  %100 = phi i32 [ 0, %44 ], [ %95, %94 ]
  tail call void @free(ptr noundef %15) #11
  br label %101

101:                                              ; preds = %4, %99
  %102 = phi i32 [ %100, %99 ], [ 0, %4 ]
  ret i32 %102
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: read)
declare i64 @strlen(ptr noundef captures(none)) local_unnamed_addr #3

; Function Attrs: mustprogress nofree nounwind willreturn allockind("alloc,uninitialized") allocsize(0) memory(inaccessiblemem: readwrite)
declare noalias noundef ptr @malloc(i64 noundef) local_unnamed_addr #4

; Function Attrs: mustprogress nounwind willreturn allockind("free") memory(argmem: readwrite, inaccessiblemem: readwrite)
declare void @free(ptr allocptr noundef captures(none)) local_unnamed_addr #5

; Function Attrs: nounwind sspstrong uwtable
define dso_local noundef i32 @main() local_unnamed_addr #6 {
  %1 = alloca [10 x i32], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #11
  %2 = call i32 @kmp_search(ptr noundef nonnull @.str, ptr noundef nonnull @.str.1, ptr noundef nonnull %1, i32 noundef 10)
  %3 = icmp eq i32 %2, 2
  br i1 %3, label %5, label %4

4:                                                ; preds = %0
  tail call void @__assert_fail(ptr noundef nonnull @.str.2, ptr noundef nonnull @.str.3, i32 noundef 72, ptr noundef nonnull @__PRETTY_FUNCTION__.main) #12
  unreachable

5:                                                ; preds = %0
  %6 = load i32, ptr %1, align 16, !tbaa !5
  %7 = icmp eq i32 %6, 10
  br i1 %7, label %9, label %8

8:                                                ; preds = %5
  tail call void @__assert_fail(ptr noundef nonnull @.str.4, ptr noundef nonnull @.str.3, i32 noundef 73, ptr noundef nonnull @__PRETTY_FUNCTION__.main) #12
  unreachable

9:                                                ; preds = %5
  %10 = getelementptr inbounds nuw i8, ptr %1, i64 4
  %11 = load i32, ptr %10, align 4, !tbaa !5
  %12 = icmp eq i32 %11, 19
  br i1 %12, label %14, label %13

13:                                               ; preds = %9
  tail call void @__assert_fail(ptr noundef nonnull @.str.5, ptr noundef nonnull @.str.3, i32 noundef 74, ptr noundef nonnull @__PRETTY_FUNCTION__.main) #12
  unreachable

14:                                               ; preds = %9
  %15 = tail call i32 (ptr, ...) @printf(ptr noundef nonnull dereferenceable(1) @.str.6, i32 noundef 10, i32 noundef 19)
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #11
  ret i32 0
}

; Function Attrs: cold noreturn nounwind
declare void @__assert_fail(ptr noundef, ptr noundef, i32 noundef, ptr noundef) local_unnamed_addr #7

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr noundef readonly captures(none), ...) local_unnamed_addr #8

attributes #0 = { nofree norecurse nosync nounwind sspstrong memory(argmem: readwrite) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nounwind sspstrong memory(readwrite, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: read) "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { mustprogress nofree nounwind willreturn allockind("alloc,uninitialized") allocsize(0) memory(inaccessiblemem: readwrite) "alloc-family"="malloc" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { mustprogress nounwind willreturn allockind("free") memory(argmem: readwrite, inaccessiblemem: readwrite) "alloc-family"="malloc" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #6 = { nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #7 = { cold noreturn nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #8 = { nofree nounwind "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #9 = { nounwind willreturn memory(read) }
attributes #10 = { nounwind allocsize(0) }
attributes #11 = { nounwind }
attributes #12 = { cold noreturn nounwind }

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
